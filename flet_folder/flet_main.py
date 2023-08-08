import flet as ft

def main(page: ft.Page):
    page.title = "A simple DataTable"            


    page.add(ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("First name")),
                    ],
            rows=[
                ft.DataRow(cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                        ],
                ),
            ],
        )
    )
ft.app(target=main)            
