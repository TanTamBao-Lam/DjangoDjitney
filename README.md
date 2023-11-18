# The Django Djitney
The Codes-ville Official Department of Transportation needs your help! They recently finished building the routes for their new commuter train, the Django Djitney, and need someone to create an easy-to-use site for commuters to be able to see the train routes. They’ve supplied the train routes in a database, but they need your help to create a site that they can use to show the different routes across all the stations, as well as update them when there are changes in the routes.

Each jitney line takes different routes through the stations. You can take a look through models.py to see how each model relates to each other. But the basic breakdown is that a “stop” consists of a “line”, a “station”, and a “stop number”.

The town wishes to have the ability to view, edit, update, and delete lines, stops, and stations. They’ve outsourced the creation of the templates, and they’ve supplied the models on their own. All you’ll need to do is create the views and link them up to the templates.

## Instructions
### Understand the Context
1. The project has been pre-populated with everything required to run the application except the views and the URLs.
Take a look at the models for the **routes** app. There should be three: `Line`, `Station`, and `Stop`.
Examine their fields, and take a look at the comments to understand what each field represents and how the models are connected to one another.

2. Take a look at the templates that have been provided. All of the templates already exist for all of the views that you will need to create. The templates also help to indicate what paths you will need to make in **routes/urls.py**, and what objects will need to be available for each page.

3. The forms for the **routes** app will come in handy when you need to implement your _“Create”_ and _“Update”_ views. Look over **forms.py** to see how this file will be used in the overall project.

4. Now navigate to **views.py** to see what’s imported for you and the provided class. After you’ve taken a look at the setup that’s been provided, let’s try to run the provided code and see what happens in the browser! As you add your own code, run it so that you can see the application update while you work on it.

### Implement the views for Lines
5. The town has named each of their jitney **lines** after different species of python! The town currently has three lines in its database. We’ll create a `ListView` that can display the different lines using the **routes/lines.html** template. Then we’ll add a `CreateView`, `UpdateView`, and `DeleteView` to allow the town to edit the lines as they please.
Let’s start by importing all of the generics we’ll require. You should have opened **routes/views.py**, import the `ListView`, `CreateView`, `UpdateView`, and `DeleteView`.

6. The `Line` model is already imported in **routes/views.py**, from `.models`.
Create a new `LinesView` class that inherits from the `ListView` you imported. Populate the `template_name` and `model` attributes of your class to bind the **routes/lines.html** template and `Line` model to your class.

7. Notice that your code didn’t do anything just yet – that’s because you need a `path`.
In **routes/urls.py**, add a `path` that calls the `LinesView` we made as a function. Your path should ensure that your page is visible at `lines/`. Use the **routes/base.html** template (with the `<nav>` inside linking to each of the pages) to infer what the `name` attribute for that `path` should be.

8. Now that you’ve got your `ListView`, you need to add the functionality to be able to **create** a new jitney line. You’ll need to:
* Add a `CreateLineView` class that uses the `CreateView` generic.
  - Make sure it uses the `Line` model!
* Add fields to `CreateLineView` that specify:
  - `form_class` as `LineForm` (this is already imported for you and you can see the forms in **routes/forms.py**).
  - `template_name` as `"routes/add_line.html"`.
* Add a new `path` for this view in **routes/urls.py**.
  - For the `name` argument, look over **routes/lines.html** to find the `name` that the template expects for the `CreateLineView`.
  - Ensure that the page is available at `"lines/new/"`.

9. Create an `UpdateLineView` to help Codes-ville change the name of their jitney lines at their leisure. You’ll need to:
* Add an `UpdateLineView` class to **routes/views.py** that inherits from the `UpdateView` generic to update the `Line` model
  - Add a field that tells the view to use the routes/update_line.html template.
  - Add another field tells the view to use the LineForm that you imported in the previous step.
* Add a new `path` for this view in **routes/urls.py**.
  - For the `name` argument, look over **routes/lines.html** to find the `name` that the template expects for the `UpdateLineView`.
  - Ensure that the page is available at `"lines/<pk>/update/"`.

10. The town should also be able to delete any lines that have to be decommissioned.

    Create a `DeleteLineView` that they can use for this. Follow the general pattern for adding a new View, and specifically for `DeleteLineView`, add a `success_url` property with a value of `"/lines"`.

    Then, add a path so that the view is accessible at `"lines/<pk>/delete/"` with `name="delete_line"`.

11. Before you can test the functionality you’ve built for viewing, creating, updating, and deleting lines, you’ll have to edit the **base** template to uncomment the link corresponding to lines in the navbar.

    Navigate to **routes/base.html** and find the `<nav>` element. You’ll notice that the links for the `lines`, `stations`, and `stops` pages are commented out. Uncomment only the lines link in the `<nav>`, and then refresh the application in the browser pane on the right.

    You can check if your `LinesView` worked by navigating to `localhost:8000/lines` in the web browser, or clicking that link in the navbar. You should see the three jitney lines that have been installed by the town and you have a `+` button to add new `Line`!

12. Test your `CreateLineView` by adding some new lines. Hit the add button below the lines table, and add a new line called _“Carpet”_, and another called _“Green Tree”_. These should show up in the lines table now, thanks to the `LinesView` we created earlier.

    Now, the town wishes to be more specific with the name of the “Carpet” line, and rename it to the ***“Jungle Carpet”*** line to indicate the correct subspecies. Click on the **Carpet** line in your lines table to be taken to your update page and validate that you can rename it to **Jungle Carpet**.

    Lastly, validate your `DeleteLineView` by clicking the ❌ next to the “Green Tree” route. Codes-ville has agreed that four lines is more than enough to service their commuters for now. After you’ve confirmed the delete, “Green Tree” should no longer appear in the lines table.

### Implement the views for Stations
13. Now that your lines are all set up, you’ll need to be able to view, create, update, and delete the **stations** that these lines will visit. You should already have seen these stations populated on the **home** page and **lines** page, but now you’ll give them their own table on their own page. Similar to what we did for **lines**:
* Start by creating a ListView. Create a new view called StationsView.
* Bind it to the Station model, and use the routes/stations.html template.
* Add a path to routes/urls.py so that we can access our StationsView at "stations/"

14. Implement the `CreateStationView`, so that the town will be able to add new stations as they come into operation.
The `CreateStationView` should:
* inherit from the CreateView generic
* use the Station model
* use the routes/add_station.html template
* use the StationForm (imported from .forms like you did with LineForm)
* have a path so that you can use it at "stations/new/", with the name as specified by the routes/stations.html template on the “add” button

15. The `Station` model has an additional field: `accessible`. The town uses this to indicate whether or not the station has accessibility features for their commuters, such as elevators or wheelchair-accessible entryways to the jitney platforms.
Implement an `UpdateStationView`, so that as the town of Codes-ville adds accessible accommodations to their older stations, they’re able to update the database to reflect the improvements.
The `UpdateStationView` should:
* inherit from the `UpdateView` generic
* use the `Station` model
* use the **routes/update_station.html** template
* use the `StationForm` like you did for the `CreateStationView`
* have a `path` at `"stations/<pk>/update/"`, with the `name` as specified in **routes/stations.html** on each entry of the station table.

16. Implement a `DeleteStationView`, so that the town can delete the stations that are just too out-of-date to be renovated and must be demolished.
The `DeleteStationView` should:
* inherit from the `DeleteView` generic
* use the `Station` model
* use the **routes/delete_station.html** template
* have a `success_url` of `"/stations/"`
* have a `path` at `"stations/<pk>/delete/"` with the name that’s used on the ❌ button in the **routes/stations.html** template

17. The functionality for viewing, creating, updating, and deleting stations for the Django Djitney rail system should be complete! Time to test out your functionality.
Like we did for **lines**, update the **routes/base.html** template to uncomment the link in the `<nav>` for `stations`. Then, when you refresh, you should be able to see the new link in your app’s navbar to test out the functionality you’ve implemented for stations!
If your views were correct, you should see a new entry in the app’s navbar now, **Stations** that you can click to view all the stations that the town currently has in place. This is your `StationsView` at work!

18. Let’s try adding a new station. Use the “add” button under the table to test out your `CreateStationView`, by adding a new _accessible_ station, **Basuto** station.

19. The town of Codes-ville has done some renovations! The ***Exmoor*** station is now accessible.
Use your `UpdateStationView` to update the **Exmoor** station so that it is marked in the stations table as accessible.

20. The **Exmoor** station is remarkably close to the worn-down **Kerry Bog** station. Since the town’s new **Exmoor** station is newer and accessible, they’ve decided to demolish the **Kerry Bog** station.
Use your `DeleteStationView` to delete the **Kerry Bog** station.
After this, you’ll have tested all the functionality you’ve implemented for stations!

### Implement the views for Stops
21. **Stops** are used to create a route for a jitney **line** through the different **stations**. As you did for lines and stations, you’ll need to create the views and add URLs so that the town can manage the stops for the jitney line. Like before, start with the `ListView`. You should:
* Create a `StopsView` that inherits from the `ListView` generic
* Set the `model` as `Stop`
* Use the template at **routes/stops.html** for your `StopsView`
* Make the page available at `"stops/"` using a `path` with `name="stops"`

22. Implement a `CreateStopView`, so that the town can add stations to different jitney routes.
Your view should:
* inherit from the `CreateView` generic
* use the `Stop` model
* use the `StopForm`, imported from `.forms`
* use the template at **routes/add_stop.html**
* be used in a `path` available at `"stops/new/"`, with `name="create_stop"`

23. Now, add an `UpdateStopView`, so that the town can change stop numbers around to make routes more convenient for commuters during rush hour.
The `UpdateStopView` should:
* inherit from the `UpdateView` generic
* use the `Stop` model
* use the `StopForm`, imported from .forms
* use the template at **routes/update_stop.html**
* be available in a path at `"stops/<pk>/update/"`, with `name="update_stop"`

24. Lastly, you’ll need to add a `DeleteStopView`. Using what you’ve learned, set the:
* generic this class will inherit from
* the model
* the template
* a `success_url`
* the correct `path()`

25. Time to test out your functionality! Like you did before, you’ll have to uncomment the link in the `<nav>` for **stops**.
Once you do that and refresh the browser, you’ll see a new link, **Stops**, in the navbar. Click it to see what your stops page looks like!
Check for any errors, and try to view your stops. After that, try to insert a stop at **Basuto** station on the **Monty** line, between **Cob** and **Anadolu** station.
To do this:
* Update stop number **6** on the Monty line at Anadolu station to have stop number **7** instead.
* Add a new stop, with:
  - the line set to Monty
  - the station set to Basuto
  - the stop number set to 6

### Djazz It Up!
26. Congratulations! You’ve completed your app for The Django Djitney. The town of Codes-ville owes you a sincere thanks!
Now that you’ve implemented the base functionality for the app, here are some things you can try to enhance the app:
* Add a `color` field to lines, like you may have seen on your local public transportation lines. Update the templates so that the text of each line in the **Lines** table is colored according to the line’s color.
* Add more fields to a station, such as **age** or **last_cleaned_date**, to help the town manage the maintenance for the stations. Update the templates so that these fields are shown on the **Stations** table
* Update the models and views to add a **schedule** to the jitney lines. Show the times that each train will stop at a given station.
