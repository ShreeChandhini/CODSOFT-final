import numpy as np

# User-item matrix
user_item_matrix = np.array([
    [5, 4, 0, 0, 1],
    [0, 3, 4, 0, 0],
    [1, 0, 0, 5, 2],
    [0, 0, 4, 0, 0],
    [0, 0, 5, 4, 0]
])

# Similarity matrix
similarity_matrix = np.dot(user_item_matrix, user_item_matrix.T)

# Recommend items for a user
def recommend_items(user_id, num_recommendations):
    user_index = user_id - 1
    user_ratings = user_item_matrix[user_index]
    similar_users = similarity_matrix[user_index]
    sorted_indices = np.argsort(similar_users)[::-1]
    
    recommendations = []
    for index in sorted_indices:
        if user_ratings[index] == 0:
            recommendations.append(index + 1)
        if len(recommendations) == num_recommendations:
            break
    
    return recommendations

# Example usage
user_id = 1
num_recommendations = 3
recommendations = recommend_items(user_id, num_recommendations)
print("Recommendations for User", user_id, ":", recommendations)