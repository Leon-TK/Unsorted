#pragma once
#include "include.h"
#include "Macros.h"
#include "Globals.h"

namespace NSPS {
    namespace Config
    {
        namespace Parser
        {
            std::pair<std::string, std::string> FindToken() {}; //name, definition
            std::string GetName() {};   
        } // namespace Parser
        
    } // namespace Config
    
};