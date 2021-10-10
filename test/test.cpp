
#include "html_imshow.hpp"

int main(void)
{

    HtmlImshow hi("test.html");
    hi.CreateHeader("Image View Test", "jp");
    hi.CreateFooter();

    HtmlImshow::ImageInfo info;
    info.title = "Lenna";
    info.width = 256;
    info.height = 256;
    hi.AddImageViewSpace("../image/sample/Lenna.bmp", info);

    info.title="Balloon";
    hi.AddImageViewSpace("../image/sample/Balloon.bmp", info);

    info.title="Aerial";
    hi.AddImageViewSpace("../image/sample/Aerial.bmp", info);

    hi.OutputToHtml();


    return(0);
}