# Shoe Catalog README
This source code is a Python web application that can be installed using the instructions found below. The source code aims to create a web application that allows users to create, read, update, and write information on the page, regarding shoes brands and models, in an authorized and authenticated manner.

## Requirements
* Vagrant
* VirtualBox
* Terminal
* Google Account (to create, update, and delete data) 

## How to use:
(Assuming you have installed the Requirements by their **default** settings...)
1. Download all files from this repository from this repository.
2. Put all files into a new directory called 'vagrant' inside another directory. (ie "Downloads/shoecatalog/vagrant")
4. Open Terminal and navigate to the previous directory
5. Type "vagrant up" followed by "vagrant ssh"
7. Type in, "cd /vagrant".
8. Type in "python final_project.py" and press Enter. This will connect to your installed database server.
9. Now using any web browser type in "localhost:8000/" on the search bar.
10. Explore the site and feel free to make your own additions

## Additional Notes:
* Any user on the application can view brands and shoe models
* In order to add, update, or delete a brand/shoe model, one must login with an authentic Google account
* Authenticated users can only update or delete their own data
