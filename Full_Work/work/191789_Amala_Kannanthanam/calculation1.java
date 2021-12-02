public class Calculation1
{
	int percentage;
	int median;
	double average;
	int min;
	int max;
	public void methods(int a)
	{
		System.out.println("percentage: " +(percentage=(a/100)) +"%");
	}
	public void methods(int b, int c,int d,int o,int q, int w)
	{

		System.out.println("median :" +(median=(b+c+d+o+q+w)/2));
	}
	public void methods(int e,int f,int g,int h,int i)
	{
		System.out.println("avaerage:" +(average=(e+f+g+h+i)/5));
	}
	public void methods(int j,int k,int l)
	{
		if((j<k)&&(j<l))
		{
		System.out.println(j+"less");}
		else if((k<j)&&(k<l)){
		System.out.println(k+"less");}
		else{
		System.out.println(l+"less");}
	}
	public void methods(int m, int n)
	{
		if(m>n)
			System.out.println(m+"Great");
		else
			System.out.println(n+"Great");
	}
	public static void main(String args[])
	{
		Calculation1 r = new Calculation1();
		r.methods(900);
		r.methods(1,2,3,4,5,6);
		r.methods(1,2,3,4,5);
		r.methods(1,2,3);
		r.methods(1,2);
	}
}