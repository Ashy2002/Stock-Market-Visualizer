"""
Stock Market Visualizer

A desktop application built with Flet that retrieves and visualizes
historical stock price data using the Alpha Vantage API.
"""

import flet as ft
from app.config import API_KEY
from app.services.stock_service import fetch_daily_stock_data


def main(page: ft.Page):
    page.title = "Stock Market Visualizer"
    page.window_width = 1000
    page.window_height = 700
    page.padding = 20

    stock_input = ft.TextField(label="Stock Symbol", width=250)
    range_dropdown = ft.Dropdown(
        label="Time Range",
        width=150,
        options=[
            ft.dropdown.Option("7"),
            ft.dropdown.Option("30"),
            ft.dropdown.Option("90"),
            ft.dropdown.Option("365"),
            ft.dropdown.Option("1825"),
        ],
        value="30",
    )

    output_text = ft.Text("", color=ft.Colors.RED)
    chart_container = ft.Container()

    def load_stock_data(e):
        stock_symbol = stock_input.value.upper().strip()
        days = int(range_dropdown.value)

        if not stock_symbol:
            output_text.value = "Please enter a stock symbol."
            page.update()
            return

        try:
            # Fetch daily stock data from Alpha Vantage API
            data = fetch_daily_stock_data(stock_symbol, API_KEY)

            dates = sorted(data.keys())[-days:]
            closes = [float(data[d]["4. close"]) for d in dates]

            if not closes:
                raise Exception("No stock data available for selected range.")

            # Prepare and render line chart for closing prices
            chart = ft.LineChart(
                data_series=[
                    ft.LineChartData(
                        data_points=[
                            ft.LineChartDataPoint(i, closes[i])
                            for i in range(len(closes))
                        ],
                        stroke_width=3,
                        color=ft.Colors.BLUE,
                    )
                ],
                min_y=min(closes) * 0.95,
                max_y=max(closes) * 1.05,
                expand=True,
            )

            chart_container.content = ft.Column(
                [
                    ft.Text(
                        f"{stock_symbol} Closing Prices",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                    ),
                    chart,
                ]
            )

            output_text.value = ""

        except Exception as ex:
            chart_container.content = None
            output_text.value = str(ex)

        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("Stock Market Visualizer", size=24, weight=ft.FontWeight.BOLD),
                ft.Row(
                    [
                        stock_input,
                        range_dropdown,
                        ft.ElevatedButton("Get Data", on_click=load_stock_data),
                    ]
                ),
                output_text,
                chart_container,
            ],
            spacing=20,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)