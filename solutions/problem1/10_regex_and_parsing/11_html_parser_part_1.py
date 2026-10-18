from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def _print_attrs(self, attrs):
        for name, value in attrs:
            print("->", name, ">", value)

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self._print_attrs(attrs)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self._print_attrs(attrs)


parser = MyHTMLParser()
parser.feed("\n".join(input() for _ in range(int(input()))))
parser.close()
