# ML-LAT-NG-Analysis
ML Project to analysis diffrence between NG and OK parts from workshop based on their production DATA
<h1> Problem description </h1>
Some pieces have been classified as not good on workshop. The classification results from the distribution of pressure over time. Pressure is checked in 3 points in time. The problem is to analyze the production data of ok and ng pieces and find the relationship that causes the pieces to be wrong. 

Main data file from workshop is constructed as:

<img src="https://user-images.githubusercontent.com/109242797/216564770-05948937-982a-4965-9ae3-ac226931b9fc.png" alt='not found' title='Main_Data_File'>

It contains:
<ol>
<li>Lot number - it is the set of pieces in which the piece was produced </li>
<li>Piece number - piece number which we analyse </li>
<li>Judgement - is it OK or NG on workshop</li>
</ol>
Additionaly there are 3 separated test temperatures (H - High, A - Ambient, L - Low). Each temperature has separated main data sheet.
<img src="https://user-images.githubusercontent.com/109242797/216568808-2330c1ce-d6ef-4eef-9ba3-1a8421691633.png" alt='not found' title='LAH Sheet'>

LOT File is constructed as follows:
<img src="https://user-images.githubusercontent.com/109242797/216568218-1b3cef63-2a3d-4797-a9f0-2448bb2d158f.png" alt='not found' title='LOT Data File'>
File name is a name of LOT in xlsx format.
Rows contains data for each produced piece. About 150 columns of data.
<br><br>
<h2> Steps: </h2> 
<ul>
<li>First point is to check OK/NG s/n from workshop and collect production data from separated files.</li>
<li>Second point is to analyze it using ML Methods.</li>
<li>Third point is to analyze it trying to predict pressure in each of 3 points of time using ML Methods.</li>
<li>Fourth point is to analyze it using DL Methods.</li>
</ul>

<h1> General OK/NG classification </h1>
This point collect all pieces (all temperatures and all gates) in one pool of data. An attempt to find a dependency without division into the test temperature and the time of occurrence of the incorrectness.
<h2> Data collection </h2>
Collect a production data for each piece from main data file using data_main.py from data.
Finally creates a new xlsx file with judgement from workshop and all production data columns generally pre-processed to avoid categorical data or data which is not crucial: <br></br>
<img src="https://user-images.githubusercontent.com/109242797/216572748-bad770f1-c6e6-4804-80ad-2d6ec53a9f0f.png" alt='not found' title='LOT Data File'>
<h2> Decision Tree Classification </h2>
First attempt to check the data using Decision Tree Classification
