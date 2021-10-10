#ifndef __HTML_IMSHOW_HPP__
#define __HTML_IMSHOW_HPP__


#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>

class HtmlImshow
{
private:

    int _space_id;
    std::string _output_file_path;
    std::string _header, _footer;
    std::vector<std::string> _image_spaces;

public:
    HtmlImshow(std::string output_file_path) : _space_id(1)
    {
        _output_file_path = output_file_path;
    }
    ~HtmlImshow(){}

    typedef struct
    {
        /* data */
        std::string title;
        int width;
        int height;
    }ImageInfo;
    


    void CreateHeader(std::string title, std::string language);
    void CreateFooter(void);
    void CreateImageViewSpace(std::string &image_space, std::string image_path, ImageInfo &info, int space_id);
    void AddImageViewSpace(std::string image_path, ImageInfo &info);

    void OutputToHtml(void);
};

#endif