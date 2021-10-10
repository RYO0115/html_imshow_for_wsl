
/**
 * @file html_imshow.cpp
 * @author RYO_UDON 
 * @brief HTML Image Viewer for WSL 
 * @version 0.1
 * @date 2021-10-10
 * 
 * @copyright Copyright (c) 2021
 * 
 */

#include "html_imshow.hpp"

/**
 * @brief Create HTML Header
 * 
 * @param title Title of the page
 * @param language Default language is "jp" (japanese).
 */
void HtmlImshow::CreateHeader(std::string title, std::string language="jp")
{
    //std::string header;
    _header = "<!DOCTYPE html>\n<html lang=" 
                + language 
                + "\n\t<head>\n"
                + "\t\t<title>\n"
                + "\t\t\t" + title + "\n"
                + "\t\t</title>\n"
                + "\t</head>\n"
                + "\t<body> \n";
    //return(header);
}

/**
 * @brief Create HTML Footer
 * 
 */
void HtmlImshow::CreateFooter(void)
{
    _footer = "\t</body\n</html>";
}


/**
 * @brief Create HTML Image View Space 
 * 
 * @param image_space [out] image space html code
 * @param image_path [in] path of image to show
 * @param info [in] Infotmation of image(title, width, height)
 * @param space_id priority id of html space (optional)
 */
void HtmlImshow::CreateImageViewSpace(std::string &image_space, std::string image_path, ImageInfo &info, int space_id=1)
{
    image_space = "\t\t<h" + std::to_string(space_id) + ">" + info.title + "</h" + std::to_string(space_id) + ">\n"
                    +"\t\t<img src=\"" + image_path + "\" "
                    +"width=\"" + std::to_string(info.width) + "\" "
                    +"height=\"" + std::to_string(info.height) + "\" "
                    +">\n";
                    
}


/**
 * @brief Add Image View Space in HTML file
 * 
 * @param image_path path of image to show
 * @param info Information of image (title, width, height)
 */

void HtmlImshow::AddImageViewSpace(std::string image_path, ImageInfo &info)
{
    std::string image_space;
    CreateImageViewSpace(image_space, image_path, info, _space_id);
    _image_spaces.push_back(image_space);
    //_space_id++;
}

/**
 * @brief Create HTML File to show image
 * 
 */

void HtmlImshow::OutputToHtml(void)
{
    std::ofstream outputfile(_output_file_path);
    outputfile << _header;
    for(int i=0; i < _image_spaces.size(); i++)
    {
        outputfile << _image_spaces[i];
    }
    outputfile << _footer;

    outputfile.close();

}

