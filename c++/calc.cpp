#include <iostream>

int a {};
int b {};
int q {};
float forward_rate_constant {};
float reverse_rate_constant {};


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
        formula();
}


