function gita(){
 output_temp=$(git diff --name-only HEAD)
 git add * 
 echo "commiting $output_temp file "
 git commit -m "$output_temp" 
 git push
}


function convert_notebooks(){
	python -c 'import os; [os.system("jupyter nbconvert --to pdf " + f) for f in os.listdir (".") if f.endswith("ipynb")]'
	pdfjam *pdf -o $@
}

function alarm(){
	sleep $@ && play ~/Downloads/old-fashioned-school-bell-daniel_simon.mp3
}%    