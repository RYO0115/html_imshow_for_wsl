
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
    hi.AddImageViewSpace("../image/color/Lenna.bmp", info);

    info.title="Balloon";
    hi.AddImageViewSpace("../image/color/Balloon.bmp", info);

    info.title="Aerial";
    hi.AddImageViewSpace("../image/color/Aerial.bmp", info);

    hi.OutputToHtml();


    return(0);
}