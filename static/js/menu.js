/**
 * Created by song on 2017/1/20.
 */
window.onload=function()
{
	var oDiv=document.getElementById("menu");
	var aBtn=oDiv.getElementsByTagName("a");

	for(var i=0;i<aBtn.length;i++)
	{
		aBtn[i].index=i;
		aBtn[i].onclick=function()
		{
			//alert(this.value);
			for(var i=0;i<aBtn.length;i++)
			{
				aBtn[i].className="";
			}
			this.className="current";

		};

    }

};
