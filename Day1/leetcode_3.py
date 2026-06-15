#include <string.h>
#include <stdbool.h>

bool isValid(char* s) {
    int length = strlen(s);
    char stack[length];
    int k = 0;

    for (int i = 0; i < length; i++) {
        
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            stack[k++] = s[i];
        } 
        
        else if (s[i] == ')' || s[i] == '}' || s[i] == ']') {
            if (k == 0) return false; 
            
            char top = stack[--k]; 
            if ((s[i] == ')' && top != '(') || 
                (s[i] == '}' && top != '{') || 
                (s[i] == ']' && top != '[')) {
                return false;
            }
        }
    }
    
    return k == 0;
}
