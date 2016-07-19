public class goldbach {
	public boolean isPrime(int n) {
		int i;
		if(n==1)
			return false;
		else if(n==2)
			return true;
		else if(n%2==0)
			return false;
		for(i=3;i<n/2;i+=2) {
			if(n%i==0)
				return false;
		}
		return true;
	}
	public int nextPrime(int n) {
		n++;
		while(true) {
			if(isPrime(n)==true)
				return n;
			n++;
		}
	}
	public boolean isGoldbach(int n) {
		if(isPrime(n)==true||n%2==0)
			return true;
		int prime=nextPrime(3),p,ans;
		while(prime<=n) {
			p=1;
			while(2*p*p+prime<=n){
				
				ans=2*p*p+prime;
				//System.out.println("ans is"+ans+" n is"+n+" p is"+ p+" prime is"+prime);
				if(ans==n){
					
					return true;
				}
				p++;
			}
			
			prime=nextPrime(prime);
		}
		return false;

	}
	public static void main(String args[]){
		goldbach g=new goldbach();
		int n=23;
		while(g.isGoldbach(n)!=false){

			n++;
		}
		System.out.println(n);
	}
}
