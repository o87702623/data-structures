package application;

import java.util.Arrays;

public class Arrays3
{
	public static void main(String[] args) 
	{
		String[] fruits = {"banana", "pear", "strawberry", "apple"};
		
		//1
		for (String fruit: fruits)
		{
			System.out.println(fruit);
		}
		
		//2
		Arrays.stream(fruits).forEach(fruit -> {
			System.out.println(fruit);
		});
	}
}
