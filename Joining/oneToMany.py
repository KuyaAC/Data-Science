# One to many
ward_license = wards.merge(license, on='ward', suffixes=('_ward','_lic'))