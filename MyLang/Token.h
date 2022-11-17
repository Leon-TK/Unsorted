#pragma once
#include "include.h"
#include "Macros.h"
#include "Globals.h"

namespace NSPS {
    class TokenTreeNode
    {
    private:
        /* data */
    public:
        TokenTreeNode(/* args */);
        ~TokenTreeNode();
    };
    class TokenAnalyzer
    {
    private:
        /* data */
    public:
        TokenAnalyzer(/* args */);
        ~TokenAnalyzer();
    };

    namespace Tokens {
        enum class Tokens {
            Statement,
            Expression,
            Keyword
        };
        namespace Keyword
        {
            enum class Keyword {
                Branch,
                Access,
                Generic,
                Const,
                Struct,
                Data,
                Methods,
                Settings,
                B_type
             };
            namespace Branch
            {
                enum class Branch {
                    If,
                    For,
                    Switch
                };
            } // namespace Branch
            namespace Access
            {
                enum class Access {
                    Public,
                    Private,
                    Derived
                };
            } // namespace Access
            namespace Settings
            {
                enum class Settings {
                    Nodiscard
                };
            } // namespace Settings
            namespace B_type
            {
                enum class B_type {
                    Int,
                    Float,
                    String,
                    Array
                };
            } // namespace B_type
            
            
        }
        
    }
    
};