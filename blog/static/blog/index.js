function counterFunction(likes){
	alert("liked");
	var finalLikes = likes + 1;
	document.getElementById('like-btn').innerHtml = "1";

}



function display(showDisplay){
	if (showDisplay == "actual-links"){
		document.getElementById('notes-tab-files').style.background = "lightgrey";
		document.getElementById('notes-tab-questions').style.background = "white";
		document.getElementById('notes-tab-labs').style.background = "white";
		document.getElementById('notes-tab-syllabus').style.background = "white";

		document.getElementById(showDisplay).style.display = "block";
		document.getElementById('actual-links-question').style.display = "none";
		document.getElementById('actual-links-syllabus').style.display = "none";
		document.getElementById('actual-links-answer').style.display = "none";
		
	}
	else if (showDisplay == "actual-links-question"){
		document.getElementById('notes-tab-files').style.background = "white";
		document.getElementById('notes-tab-questions').style.background = "lightgrey";
		document.getElementById('notes-tab-labs').style.background = "white";
		document.getElementById('notes-tab-syllabus').style.background = "white";

		document.getElementById(showDisplay).style.display = "block";
		document.getElementById('actual-links').style.display = "none";
		document.getElementById('actual-links-syllabus').style.display = "none";
		document.getElementById('actual-links-answer').style.display = "none";
		
	}
	else if (showDisplay == "actual-links-syllabus"){

		document.getElementById('notes-tab-files').style.background = "white";
		document.getElementById('notes-tab-questions').style.background = "white";
		document.getElementById('notes-tab-labs').style.background = "white";
		document.getElementById('notes-tab-syllabus').style.background = "lightgrey";

		document.getElementById(showDisplay).style.display = "block";
		document.getElementById('actual-links').style.display = "none";
		document.getElementById('actual-links-question').style.display = "none";
		document.getElementById('actual-links-answer').style.display = "none";
		
	}
	else if (showDisplay == "actual-links-answer"){
		document.getElementById('notes-tab-files').style.background = "white";
		document.getElementById('notes-tab-labs').style.background = "lightgrey";
		document.getElementById('notes-tab-questions').style.background = "white";
		document.getElementById('notes-tab-syllabus').style.background = "white";

		document.getElementById(showDisplay).style.display = "block";
		document.getElementById('actual-links').style.display = "none";
		document.getElementById('actual-links-syllabus').style.display = "none";
		document.getElementById('actual-links-question').style.display = "none";
		
	}
	document.getElementById(offDisplay).style.display = "none";
	
	
}
