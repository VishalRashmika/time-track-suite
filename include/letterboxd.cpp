#include "letterboxd.h"
#include <iostream>

#include "gumbo.h"
#include "string.h"

int return_time;

static void find_line(const std::string& original_text, const GumboAttribute& attr) 
{
    // attr = gumbo_get_attribute(&node->v.element.attributes, "class")) && strstr(cls_attr->value, cls_name)
    // original_text.data() -------> html code  
  size_t attr_index = attr.original_value.data - original_text.data();
  //std::cout << attr.original_value.data << std::endl;
  size_t begin = original_text.rfind("\n", attr_index) + 50;
  
  size_t end = original_text.find("\n", attr_index) + 25;
  
  
  if (end != std::string::npos) {
    end--;
  } else {
    end = (size_t) original_text.length() - 1;
  }
  end = std::min(end, attr_index + 40);
  begin = std::max(begin, attr_index - 40);

    return_time = std::stoi( original_text.substr(begin, end - begin - 1));

}


static void search_for_class(GumboNode* node, const std::string& original_text, const char* cls_name){
    if (node->type != GUMBO_NODE_ELEMENT) {
    return;
    }
    GumboAttribute* cls_attr;
    
    if ((cls_attr = gumbo_get_attribute(&node->v.element.attributes, "class")) && strstr(cls_attr->value, cls_name) != NULL) 
    {
      // std::cout << cls_attr->value_start.line << ":" << cls_attr->value_start.column << " - " << find_line(original_text, *cls_attr) << std::endl;
      find_line(original_text, *cls_attr);

    }
    
    GumboVector* children = &node->v.element.children;
    for (int i = 0; i < children->length; ++i) {
      search_for_class(static_cast<GumboNode*>(children->data[i]), original_text, cls_name);
    }
}


int Letterboxd::get_time(std::string source){
  const char* cls = "text-link text-footer";

  GumboOutput* output = gumbo_parse(source.c_str()); //~ parser object
  // search_for_links(output->root); //~scraping logic happens
  search_for_class(output->root, source, cls);
  gumbo_destroy_output(&kGumboDefaultOptions, output);

  return return_time;
}

