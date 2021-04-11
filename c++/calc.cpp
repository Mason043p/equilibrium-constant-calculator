#include <iostream>

int a {};
int b {};
int q {};
float forward_rate_constant {};
float reverse_rate_constant {};
int number_of_calculations {};

void formula()
{
        a = a - a * forward_rate_constant;
        a = a + b * reverse_rate_constant;
        b = b * reverse_rate_constant + a * forward_rate_constant;
        q = b / a;
        std::cout << "A = " << a << " B = " << b << " Q = " << q << '\n';
}


int main()
{

        std::cout << "What is a's starting value?" << '\n';
        std::cin >> a;
        std::cout << "What is b's starting value?" << '\n';
        std::cin >> b;
        std::cout << "What is the value of the forward rate constant as a decimal?" << '\n';
        std::cin >> forward_rate_constant;
        std::cout << "what is the value of the reverse rate constant as a decimal?" << '\n';
        std::cin >> reverse_rate_constant;
        std::cout << "How many calculations would you like to make?" << '\n';
        std::cin >> number_of_calculations;
        
        
        for (int i=0; i < number_of_calculations  ; i++) {
                formula();
        }
}


