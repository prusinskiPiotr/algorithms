#include <iostream>
using namespace std;


class Fraction {
    private:
    int num;
    int den;

    public:
    Fraction(int top, int bottom){
        num = top;
        den = bottom;
    }

    Fraction operator +(Fraction otherFrac){
        int newnum = num*otherFrac.den + den*otherFrac.num;
        int newden = den*otherFrac.den;

        return Fraction(newnum, newden);
    }

    friend ostream& operator <<(ostream&, const Fraction& fraction);
};

ostream & operator <<(ostream& stream, const Fraction& fraction) {
    stream << fraction.num << "/" << fraction.den;

    return stream;
}

int main(){
    Fraction f1(1,4);
    Fraction f2(1,2);
    Fraction f3=f1+f2;
    cout << f3 <<endl;
    return 0;
}
