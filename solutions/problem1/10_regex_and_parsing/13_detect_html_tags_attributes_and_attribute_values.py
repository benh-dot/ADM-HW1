from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("->", name, ">", value)

    # self-closing tags (<br />) are reported the same way
    handle_startendtag = handle_starttag


parser = MyHTMLParser()
parser.feed("\n".join(input() for _ in range(int(input()))))
parser.close()
