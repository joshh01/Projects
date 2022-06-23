import java.util.HashMap;
public class IDandPasswords 
{
	HashMap<String, String> loginInfo = new HashMap<String, String>();
	IDandPasswords()
	{
		loginInfo.put("Josh", "pizza");
		loginInfo.put("Sheri", "hii");
		loginInfo.put("David", "abc123");
	}
	public void addInfo(String username, String password)
	{
		loginInfo.put(username, password);
	}
	protected HashMap<String, String> getLoginInfo()
	{
		return loginInfo;
	}
}
