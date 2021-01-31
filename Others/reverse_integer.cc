class Solution {
public:
    int reverse(int x) {

        // base cases (range)
        if(x < 10 && x > -10) return x;
        if(x >= INT_MAX || x <= INT_MIN) return 0;

        long tmp = x % 10;    // use long to check the reversed value within the int range
        while(x /= 10)
        {
            if(tmp*10 >= INT_MAX || tmp*10 <= INT_MIN) return 0;
            tmp *= 10;
            tmp += (x%10);
        }
        return tmp;

    }
};
