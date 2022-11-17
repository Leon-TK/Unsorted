#pragma once
#include "include.h"
#include "Macros.h"

namespace NSPS {
    struct Scope {
        std::string m_name = "";
        static size_t id;
        Scope* m_pParent = nullptr;
        std::vector<Scope*> m_children = {};

        Scope() {
            m_name = "Scope_" + std::to_string(Scope::id);
        }
    };

    class ScopeManager {
        Scope* m_pCurrentScope = nullptr;
        public:
        void ChangeScope(Scope* pScope) {
            m_pCurrentScope = pScope;
        };
    };

    class ScopeAnalyser {

    };

    enum class Scopes {
        File,
        Namespace,
        Function,
        Structure,
        Data,
        Behavior,
        If,
        For,
        Switch
    };
}