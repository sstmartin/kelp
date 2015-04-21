import java.util.ArrayList;
import java.util.List;

import org.json.simple.JSONObject;


public class Business {
	public String business_id = null;
	public String full_address = null;
	public JSONObject hours = null;
	public boolean open;
	public List<String> categories = null;
	public String city = null;
	public long review_count = 0;
	public String name = null;
	public List<String> neighborhoods = null;
	public double longitude = 0;
	public String state = null;
	public double stars = 0;
	public double latitude = 0;
	public JSONObject attributes = null;
	public String type = "business";
	
	public String toString() {
		return "business_id: " + business_id + "\n" 
				+ "full_address: " + full_address + "\n"
				+ "open: " + open + "\n"
				+ "categories: " + categories + "\n"
				+ "city: " + city + "\n"
				+ "review_count: " + review_count + "\n"
				+ "name: " + name + "\n"
				+ "longitude: " + longitude + "\n"
				+ "latitude: " + latitude + "\n"
				+ "state: " + state + "\n"
				+ "stars: " + stars + "\n"
				+ "attributes: " + attributes + "\n"
				+ "type: " + type;
	}
	
	public String toCSV() {
		return business_id + "|" 
				+ full_address + "|"
				+ hours + "|"
				+ open + "|"
				+ removeBars(categories.toString()) + "|"
				+ city + "|"
				+ review_count + "|"
				+ removeBars(name) + "|"
				+ neighborhoods + "|"
				+ longitude + "|"
				+ latitude + "|"
				+ state + "|"
				+ stars + "|"
				+ removeBars(attributes.toJSONString()) + "|"
				+ type;
	}
	
	String removeBars(String s) {
		
		return s.replace("|", "");
	}
}
