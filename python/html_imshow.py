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
        self.__image_spaces = [[]]
        self.__footer = ""
        self.__space_id = 0
        self.__font_size = 20
        self.__image_space_header1 = "\t\t<p style=\"float: left; font-size: "
        self.__image_space_header2 = "pt; text-align: center; width: "
        self.__image_space_header3 = "%; margin-right: " 
        self.__image_space_header4 = "%; margin-bottom: 0.5em;\"\n>"

        self.__widthp = 50
        self.__image_gap = 1
        
        #self.__image_space_header = "\t\t<div class=\"row\">\n"
        #self.__image_space_footer = "\t\t</div>\n"

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

    
    def CreateImageViewSpace(self, image_path_str, image_info):

        #image_space_html_str = "\t\t<h1>" + image_info.title + "</h1>\n" \
        #            +"\t\t<img src=\"" + image_path_str + "\" " \
        #            +"width=\"" + str(image_info.width) + "\" " \
        #            +"height=\"" +str(image_info.height) + "\" " \
        #            +">\n"
        #image_space_html_str = "\t\t\t<div class=\"column\">\n" \
        #                        + "\t\t\t\t<img src=\"" + image_path_str + "\" alt=\"" + image_info.title + "\" >\n" \
        #                        + "\t\t\t</div>\n"
        image_space_html_str = "\t\t\t\t<img src=\"" + image_path_str + "\" style=\"width:100%\"/>" + image_info.title +"</p>\n"

        return(image_space_html_str)
    
    def AddImageViewSpaceVertical(self, image_path_str, image_info):

        image_space_html_str = self.CreateImageViewSpace(image_path_str, image_info)
        self.__image_spaces[self.__space_id].append(image_space_html_str)
        self.__image_spaces.append([])
        self.__space_id += 1

    def AddImageViewSpaceHorizontal(self, image_path_str, image_info, space_id=-1):

        image_space_html_str = self.CreateImageViewSpace(image_path_str, image_info)
        if space_id == -1:
            space_id = self.__space_id - 1
        self.__image_spaces[space_id].append(image_space_html_str)
    

    def OutputToHtml(self):
        with open(self.__output_file_path, "w") as f:
            f.write(self.__header)
            for spaces in self.__image_spaces:

                for i in range(len(spaces)):
                #for html_str in spaces:
                    html_str = spaces[i]
                    width = int(self.__widthp / len(spaces))
                    f.write(self.__image_space_header1)
                    f.write(str(self.__font_size))
                    f.write(self.__image_space_header2)
                    f.write(str(width))
                    f.write(self.__image_space_header3)
                    if i == len(spaces)-1:
                        f.write(str(100 - self.__widthp - self.__image_gap))
                    else:
                        f.write(str(self.__image_gap))
                    
                    f.write(self.__image_space_header4)
                    f.write(html_str)
            f.write(self.__footer)

    def SetFontSize(self, font_size):
        self.__font_size = font_size

    def SetMaxWidthPercentage(self, widthp):
        self.__widthp = widthp

        

if __name__ == '__main__':
    hi = HtmlImshow("test.html")
    hi.CreateHeader("Image View", "jp")
    hi.CreateFooter()

    info = ImageInfo()
    info.title = "Lenna"
    hi.AddImageViewSpaceVertical("../image/sample/Lenna.bmp", info)
    hi.AddImageViewSpaceHorizontal("../image/sample/Lenna.bmp", info)
    hi.AddImageViewSpaceVertical("../image/sample/Lenna.bmp", info)
    hi.AddImageViewSpaceHorizontal("../image/sample/Lenna.bmp", info)

    hi.OutputToHtml()






