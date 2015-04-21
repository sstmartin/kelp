import org.json.simple.JSONObject;


public class Review {
	public JSONObject votes = null;
	public String user_id = null;
	public String review_id = null;
	public long stars = 0;
	public String date = null;
	public String text = null;
	public String type = "review";
	public String business_id = null;
	
	public String toString() {
		return "votes: " + votes + "\n" 
				+ "user_id: " + user_id + "\n"
				+ "review_id: " + review_id + "\n"
				+ "stars: " + stars + "\n"
				+ "date: " + date + "\n"
				+ "text: " + text + "\n"
				+ "type: " + type + "\n"
				+ "business_id: " + business_id;
	}
	
	public String toCSV() {
		return votes + "|" 
				+ user_id + "|"
				+ review_id + "|"
				+ stars + "|"
				+ date + "|"
				+ removeBars(text.replaceAll("(\\r|\\n|\\r\\n)+", "").replace("\\n", "")) + "|"
				+ type + "|"
				+ business_id;
	}
	
String removeBars(String s) {
		
		return s.replace("|", "");
	}
}
