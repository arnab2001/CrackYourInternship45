/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int T=sc.nextInt();
		for(int i=1;i<=T;i++)
		{
		    int N,X;
		    N=sc.nextInt();
		    X=sc.nextInt();
		    int slice,temp;
		    if((N%2==0) && (X%2==0))
		    {
		        slice=(N*X)/4;
		        System.out.println(slice);
		        
		    }
		    else if((N%2!=0) && (X%2!=0))
		    {
		        slice=((N*X)/4)+1;
		        System.out.println(slice);
		    }
		    else {
                slice=(N*X);
                if(slice%4==0){
                    temp=slice/4;
                    System.out.println(temp);
                }
                else{
                    temp=(slice/4) + 1;
                    System.out.println(temp);
                }
		    }
		    
		    
		}
	}
}
