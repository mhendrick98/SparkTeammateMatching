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

def main(args):
	student_id_features_dict = {}

	df_fellows = pd.read_csv('fellows_sparkx.csv')
	df_fellows = df_fellows.fillna(0)
	df_students = pd.read_csv('students_sparkx.csv')
	df_students = df_students.fillna(0)


	print(df_fellows.ix[0:0,2])
	# 0th group of fellows
	df_fellows_selected_columns_team_0 = pd.concat([df_fellows.ix[0:0,2], df_fellows.ix[0:0,129:214]],axis=1)
	print(df_fellows_selected_columns_team_0['Email'])
	# 1st group of fellows
	df_fellows_selected_columns_team_1 = pd.concat([df_fellows.ix[1:3,2], df_fellows.ix[1:3,129:214]],axis=1)
	# 2nd group of fellows
	df_fellows_selected_columns_team_2 = pd.concat([df_fellows.ix[4:4,2], df_fellows.ix[4:4,129:214]],axis=1)
	# 3rd group of fellows
	df_fellows_selected_columns_team_3 = pd.concat([df_fellows.ix[5:7,2], df_fellows.ix[5:7,129:214]],axis=1)
	# 4th group of fellows
	df_fellows_selected_columns_team_4 = pd.concat([df_fellows.ix[8:8,2], df_fellows.ix[8:8,129:214]],axis=1)
	# 5th group of fellows
	df_fellows_selected_columns_team_5 = pd.concat([df_fellows.ix[9:9,2], df_fellows.ix[9:9,129:214]],axis=1)
	# 6th group of fellows
	df_fellows_selected_columns_team_6 = pd.concat([df_fellows.ix[10:11,2], df_fellows.ix[10:11,129:214]],axis=1)
	# 7th group of fellows
	df_fellows_selected_columns_team_7 = pd.concat([df_fellows.ix[11:12,2], df_fellows.ix[11:12,129:214]],axis=1)


	df_students_selected_columns = pd.concat([df_students.ix[:,1], df_students.ix[:,35:120]],axis=1)
	df_students_selected_column_names = df_students_selected_columns.columns.values


	feature_vector_fellows_team_0 = create_feature_vector_of_fellows(df_fellows_selected_columns_team_0)
	print('Length of feature vector fellows team 0:',len(feature_vector_fellows_team_0))
	feature_vector_fellows_team_1 = create_feature_vector_of_fellows(df_fellows_selected_columns_team_1)
	print('Length of feature vector fellows team 1:',len(feature_vector_fellows_team_1))
	feature_vector_fellows_team_2 = create_feature_vector_of_fellows(df_fellows_selected_columns_team_2)
	print('Length of feature vector fellows team 2:',len(feature_vector_fellows_team_2))
	feature_vector_fellows_team_3 = create_feature_vector_of_fellows(df_fellows_selected_columns_team_3)
	print('Length of feature vector fellows team 3:',len(feature_vector_fellows_team_3))
	feature_vector_fellows_team_4 = create_feature_vector_of_fellows(df_fellows_selected_columns_team_4)
	print('Length of feature vector fellows team 4:',len(feature_vector_fellows_team_4))
	feature_vector_fellows_team_5 = create_feature_vector_of_fellows(df_fellows_selected_columns_team_5)
	print('Length of feature vector fellows team 5:',len(feature_vector_fellows_team_5))
	feature_vector_fellows_team_6 = create_feature_vector_of_fellows(df_fellows_selected_columns_team_6)
	print('Length of feature vector fellows team 6:',len(feature_vector_fellows_team_6))
	feature_vector_fellows_team_7 = create_feature_vector_of_fellows(df_fellows_selected_columns_team_7)
	print('Length of feature vector fellows team 7:',len(feature_vector_fellows_team_7))

	for index, row in df_students_selected_columns.iterrows():
		student_id_features_dict[row['Email']] = row.tolist()[1:]

	print('Computing score for team 0.')
	student_score_team_0_list = compute_each_student_scores(student_id_features_dict,feature_vector_fellows_team_0)
	print('Computing score for team 1.')
	student_score_team_1_list = compute_each_student_scores(student_id_features_dict,feature_vector_fellows_team_1)
	print('Computing score for team 2.')
	student_score_team_2_list= compute_each_student_scores(student_id_features_dict,feature_vector_fellows_team_2)
	print('Computing score for team 3.')
	student_score_team_3_list = compute_each_student_scores(student_id_features_dict,feature_vector_fellows_team_3)
	print('Computing score for team 4.')
	student_score_team_4_list = compute_each_student_scores(student_id_features_dict,feature_vector_fellows_team_4)
	print('Computing score for team 5.')
	student_score_team_5_list = compute_each_student_scores(student_id_features_dict,feature_vector_fellows_team_5)
	print('Computing score for team 6.')
	student_score_team_6_list = compute_each_student_scores(student_id_features_dict,feature_vector_fellows_team_6)
	print('Computing score for team 7.')
	student_score_team_7_list = compute_each_student_scores(student_id_features_dict,feature_vector_fellows_team_7)

	print('Writing selections for team 0.')
	write_tuple_list_to_csv('fellow1.csv',student_score_team_0_list)
	print('Writing selections for team 1.')
	write_tuple_list_to_csv('fellow2.csv',student_score_team_1_list)
	print('Writing selections for team 2.')
	write_tuple_list_to_csv('fellow3.csv',student_score_team_2_list)
	print('Writing selections for team 3.')
	write_tuple_list_to_csv('fellow4.csv',student_score_team_3_list)
	print('Writing selections for team 4.')
	write_tuple_list_to_csv('fellow5.csv',student_score_team_4_list)
	print('Writing selections for team 5.')
	write_tuple_list_to_csv('fellow5.csv',student_score_team_5_list)
	print('Writing selections for team 6.')
	write_tuple_list_to_csv('fellow6.csv',student_score_team_6_list)
	print('Writing selections for team 7.')
	write_tuple_list_to_csv('fellow7.csv',student_score_team_7_list)


if __name__ == '__main__':
	main(sys.argv[1:])
	print('Exiting main!')
