from xml.etree.ElementTree import XMLParser

class ColorValue:                     # The target object of the parser
    red = 0
    green = 0
    blue = 0
    depth = 0
    def start(self, tag, attrib):   # Called for each opening tag.
        self.depth += 1
        if attrib['color'] == "red":
            self.red += self.depth
        elif attrib['color'] == "green":
            self.green += self.depth
        else:
           self.blue += self.depth
    def end(self, tag):             # Called for each closing tag.
        self.depth -= 1
    def close(self):    # Called when all data has been parsed.
        print(self.red, self.green, self.blue)

def main():
    target = ColorValue()
    parser = XMLParser(target=target)
    exampleXml = input()
    parser.feed(exampleXml)
    parser.close()

if __name__ == "__main__":
    main()