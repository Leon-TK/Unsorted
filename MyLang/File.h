#pragma once
#include "include.h"
#include "Macros.h"
#include "Globals.h"

namespace NSPS {
    template<typename Buffer>
    struct File {
        Buffer buffer;
    }; 

    class FileManager
    {
    private:
        /* data */
    public:
        FileManager(/* args */);
        ~FileManager();
    };
    
    class FileAnalyzer
    {
    private:
        /* data */
    public:
        FileAnalyzer(/* args */);
        ~FileAnalyzer();
    };
    
};