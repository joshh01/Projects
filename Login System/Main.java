import java.io.IOException;
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

import javax.swing.JLabel;
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
		LoginPage lp = new LoginPage(idandPasswords.getLoginInfo());
		scanner.close();
		
		
		
		for(int i = 0; i < usernames.size(); i++)
		{
			JLabel label = new JLabel(usernames.get(i));
			JLabel pass = new JLabel(passwords.get(i));
			label.setBounds(5, ((i - 1) * 20) + 5, 100, 50);
			pass.setBounds(55, ((i - 1) * 20) + 5, 100, 50);
			lp.addLabel(label);
			lp.addLabel(pass);
		}
		
		
		
	}
	// Splits user:pass into user & pass
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
			// Makes sure that the string contains a ":", that there is data before and after the colon
			if(arr.get(i).contains(":") && colonIndex != 0 && colonIndex != arr.get(i).length() - 1)
			{
				username = data.substring(0, colonIndex);
				password = data.substring(colonIndex + 1, data.length());
				usernames.add(username);
				passwords.add(password);
			}
		}
	}
}
