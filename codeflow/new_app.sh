APP_NAME=$1
if [ -d "./applications/$APP_NAME" ]; then
	echo 'Application already exists.'
else
	app_file="${APP_NAME}_application.py"
	test_file="test_${app_file}"

	echo 'Creating folder structure.'

	mkdir "./applications/$APP_NAME"
	touch "./applications/$APP_NAME/$app_file"

	touch "./applications/$APP_NAME/__init__.py"

	mkdir "./applications/$APP_NAME/install_scripts"
	touch "./applications/$APP_NAME/install_scripts/install_linux_32.sh"
	chmod +x "./applications/$APP_NAME/install_scripts/install_linux_32.sh"
	touch "./applications/$APP_NAME/install_scripts/install_linux_64.sh"
	chmod +x "./applications/$APP_NAME/install_scripts/install_linux_64.sh"
fi

