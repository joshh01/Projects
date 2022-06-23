import java.io.IOException;
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;
public class Main 
{
	public static void main(String[] args) throws IOException
	{
		IDandPasswords idandPasswords = new IDandPasswords();
		Scanner scanner = new Scanner(System.in);
		Scanner file = new Scanner(new File("info.txt"));
		ArrayList<String> loginStrings = new ArrayList<String>();
		ArrayList<String> usernames = new ArrayList<String>();
		ArrayList<String> passwords = new ArrayList<String>();
		// Populates the loginStrings array list
		while(file.hasNext())
		{
			loginStrings.add(file.nextLine().trim());
		}
		split(loginStrings, usernames, passwords);
		// Adds user-names and passwords to the IDandPasswords HashMap
		for(int i = 0; i < usernames.size(); i++)
		{
			idandPasswords.addInfo(usernames.get(i), passwords.get(i));
		}
		// Creates login page
		new LoginPage(idandPasswords.getLoginInfo());
		scanner.close();
	}
	// Splits xxx:yyy into xxx & yyy
	public static void split(ArrayList<String> arr, ArrayList<String> usernames, ArrayList<String> passwords)
	{
		int colonIndex = -1;
		String password, username, data;
		for(int i = 0; i < arr.size(); i++)
		{
			data = arr.get(i);
			for(int j = 0; j < data.length(); j++)
			{
				if(arr.get(i).charAt(j) == ':')
				{
					colonIndex = j;
				}
			}
			username = data.substring(0, colonIndex);
			password = data.substring(colonIndex + 1, data.length());
			usernames.add(username);
			passwords.add(password);
		}
	}
}
