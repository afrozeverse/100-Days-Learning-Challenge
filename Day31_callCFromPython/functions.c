int lcm(int a, int b)
{
    int L;
    for (L=a>b?a:b;L<=a*b;L++)
        if(L%a==0 && L%b==0)
            return L;
    return 1;
}

int fact(int n)
{
    int f=1;
    while (n)
    {
        f=f*n;
        n--;
    }
    return f;
    
}

// This is not a normal c program, we are creating a libray, so we will not create a nomral .exe file. Here we will create a .so file. The command to do so is (change the fileName with your filename, first fileName can be anything, this will be the library name created by you.)
// gcc -std=c11 -o fileName.so --shared -fPIC fileName.c
// for this file I did >  gcc -std=c11 -o myLibrary.so --shared -fPIC functions.c