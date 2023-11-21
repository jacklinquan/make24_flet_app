"""Make 24 Flet App."""

from random import choices
import asyncio
import flet as ft

from make24_solver import solve24


class Make24App(ft.UserControl):
    TITLE = "Make 24"
    TITLE_SIZE = 24

    def __init__(self):
        super().__init__()
        self.full_num_list = [i for i in range(1, 14)]
        self.init_values = [1, 4, 5, 6]
        self.res24 = solve24(*self.init_values)

    def build(self):
        self.layout = ft.Column(
            scroll=ft.ScrollMode.ADAPTIVE,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.layout.controls.append(
            ft.Row(
                [ft.Text(self.TITLE, size=self.TITLE_SIZE)],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        self.layout.controls.append(ft.Divider(height=9, thickness=3))

        self.layout.controls.append(
            ft.ElevatedButton("Generate", on_click=self.btn_generate_handler)
        )
        self.input_nums = [
            ft.Dropdown(
                value=str(self.init_values[i]),
                width=60,
                options=[ft.dropdown.Option(f"{i}") for i in self.full_num_list],
            )
            for i in range(4)
        ]
        self.layout.controls.append(
            ft.Row(self.input_nums, alignment=ft.MainAxisAlignment.CENTER)
        )

        self.layout.controls.append(ft.Divider(height=9, thickness=1))

        self.layout.controls.append(
            ft.ElevatedButton("Solve", on_click=self.btn_solve_handler)
        )
        self.result_column = ft.Column(
            width=300,
            height=300,
            scroll=ft.ScrollMode.ADAPTIVE,
        )
        self.layout.controls.append(
            ft.Container(
                self.result_column,
                border=ft.border.all(1),
            )
        )

        return self.layout

    async def btn_generate_handler(self, e):
        done = False
        while not done:
            nums = choices(self.full_num_list, k=4)
            res24 = solve24(*nums)
            if res24:
                self.res24 = res24
                break
            await asyncio.sleep(0)

        for i in range(4):
            self.input_nums[i].value = str(nums[i])
            await self.input_nums[i].update_async()

        self.result_column.controls.clear()
        await self.result_column.update_async()

    async def btn_solve_handler(self, e):
        nums = [int(self.input_nums[i].value) for i in range(4)]
        self.res24 = solve24(*nums)

        self.result_column.controls.clear()
        self.result_column.controls.append(
            ft.Text(f"There is/are {len(self.res24)} solution(s) in total.")
        )
        for i in range(len(self.res24)):
            self.result_column.controls.append(ft.Text(self.res24[i]))
        await self.result_column.update_async()


async def main(page):
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.BLUE))
    page.title = Make24App.TITLE
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.alignment = ft.MainAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    await page.update_async()

    await page.add_async(Make24App())


ft.app(main)
