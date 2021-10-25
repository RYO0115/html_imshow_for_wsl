import os,sys


class ImageInfo:
    def __init__(self):
        self.title = ""
        self.width = 0
        self.height = 0

class HtmlImshow:
    def __init__(self, output_file_path):
        self.__output_file_path = output_file_path
        self.__header = ""
        self.__image_spaces = []
        self.__footer = ""
        self.__space_id = 1

    def CreateHeader(self, title, language="jp"):
        self.__header = "<!DOCTYPE html>\n<html lang=" \
                    + language \
                    + "\n\t<head>\n" \
                    + "\t\t<title>\n" \
                    + "\t\t\t" + title + "\n" \
                    + "\t\t</title>\n" \
                    + "\t</head>\n" \
                    + "\t<body> \n"
    
    def CreateFooter(self):
        self.__footer = "\t</body\n</html>"

    
    def CreateImageViewSpace(self, image_path_str, image_info, space_id):

        image_space_html_str = "\t\t<h" + str(space_id) + ">" + image_info.title + "</h" + str(space_id) + ">\n" \
                    +"\t\t<img src=\"" + image_path_str + "\" " \
                    +"width=\"" + str(image_info.width) + "\" " \
                    +"height=\"" +str(image_info.height) + "\" " \
                    +">\n"

        return(image_space_html_str)
    
    def AddImageViewSpace(self, image_path_str, image_info):

        image_space_html_str = self.CreateImageViewSpace(image_path_str, image_info, self.__space_id)
        self.__image_spaces.append(image_space_html_str)


    
    def OutputToHtml(self):
        with open(self.__output_file_path, "w") as f:
            f.write(self.__header)
            for html_str in self.__image_spaces:
                f.write(html_str)
            f.write(self.__footer)

        

if __name__ == '__main__':
    hi = HtmlImshow("test.html")
    hi.CreateHeader("Image View", "jp")
    hi.CreateFooter()

    info = ImageInfo()
    info.title = "Lenna"
    info.width = 256
    info.height = 256
    hi.AddImageViewSpace("../image/sample/Lenna.bmp", info)

    hi.OutputToHtml()






