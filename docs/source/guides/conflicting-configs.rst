Conflicting Configs
===================

When using multiple configs, this leaves the opportunity of clashing config keys.

When two keys clash in value there are few things that can happen:
    * If one of the two values isn't a object/dict, the newest value is dropped.
    * If both values are object/dict, they will be recursively merged.
        * If there is a conflicting key, that don't share the same value. A ValueError is raised.
