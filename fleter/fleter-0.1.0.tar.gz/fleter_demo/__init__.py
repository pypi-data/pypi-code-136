import flet
import fleter


def run():
    def main(page: flet.Page):
        headerBar = fleter.HeaderBar(page, )
        headerBar.show()
        headerBar.controls.insert(1, fleter.SwichThemeButton(page))
        page.update()

    flet.app(target=main)


if __name__ == '__main__':
    run()
