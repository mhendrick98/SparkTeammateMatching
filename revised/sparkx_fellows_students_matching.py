# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
from scipy.spatial import distance

import csv
import pandas as pd
import sys

def create_feature_vector_of_fellows(df):
	feature_vector = df.mean().round(2).tolist()
	return feature_vector

def compute_each_student_scores(student_dict,feature_vector_fellow):
	student_score_list = []
	for email, feat_vector_student in student_dict.items():
		tup = (email,distance.euclidean(feat_vector_student, feature_vector_fellow))
		student_score_list.append(tup)

	student_score_list.sort(key=lambda x: x[1], reverse = False)
	return student_score_list

def write_tuple_list_to_csv(filename,data):
	with open(filename,'w') as out:
		csv_out=csv.writer(out)
		csv_out.writerow(['email','distance_score'])
		for row in data:
			csv_out.writerow(row)

def main(args, fellowsCSV, xlabCSV):
	student_id_features_dict = {}

	df_fellows = pd.read_csv(fellowsCSV)
	df_fellows = df_fellows.fillna(0)
	df_students = pd.read_csv(xlabCSV)
	df_students = df_students.fillna(0)

	num_of_fellows = 9

	for i in range(0, num_of_fellows):
		temp_fellows_selected_columns_team = pd.concat([df_fellows.ix[i:i,1], df_fellows.ix[i:i,2:]],axis=1)
		df_students_selected_columns = pd.concat([df_students.ix[:,2], df_students.ix[:,3:-7]],axis=1)
		df_students_selected_column_names = df_students_selected_columns.columns.values
		temp_feature_vector_fellows_team = create_feature_vector_of_fellows(temp_fellows_selected_columns_team)
		for index, row in df_students_selected_columns.iterrows():
			student_id_features_dict[row['Email']] = row.tolist()[1:]
		student_score_team_temp_list = compute_each_student_scores(student_id_features_dict,temp_feature_vector_fellows_team)
		team_name = df_fellows.ix[i:i,0].values[0]
		file_name = team_name + " Scores.csv"
		write_tuple_list_to_csv(file_name,student_score_team_temp_list)


if __name__ == '__main__':
	main(sys.argv[1:], 'fellows_sparkx.csv', 'xlab_sparkx.csv')
	print('Exiting main!')
