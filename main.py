import flet as ft
from llama_cpp import Llama


def main(page: ft.Page):
    page.padding = 16

    def ai_llama():
        code_llm = Llama(
            model_path="/path/to/your/llm",
            chat_format="llama-2",
            n_ctx=0,
        )
        complition = code_llm.create_chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant",
                },
                {
                    "role": "user",
                    "content": text_field.value,
                },
            ],
            max_tokens=0,
            temperature=0.2,
            top_p=0.1,
        )
        return complition["choices"][0]["message"]["content"].strip()

    def res_ai(e):
        prog_ring.visible = True
        page.update()
        res = ai_llama()
        prog_ring.visible = False
        res_text.value = res
        page.update()

    prog_ring = ft.Stack(
        [
            ft.Column(
                [
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.ProgressRing(
                                    bgcolor="blue100",
                                    height=60,
                                    width=60,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        expand=True,
        visible=False,
    )

    text_field = ft.TextField(
        multiline=True,
        max_lines=5,
        expand=True,
        hint_text="Ask The AI Model...",
        text_style=ft.TextStyle(italic=True, weight="bold", size=18),
    )

    send_btn = ft.Container(
        content=ft.IconButton(
            icon="send",
            icon_size=44,
            icon_color=ft.colors.BLUE_GREY_800,
            on_click=res_ai,
        )
    )
    res_text = ft.Text(
        size=18,
        weight="bold",
        selectable=True,
    )

    page.add(
        ft.Stack(
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                text_field,
                                send_btn,
                            ]
                        ),
                        res_text,
                    ]
                ),
                prog_ring,
            ],
            expand=True,
        )
    )


ft.app(main)
