from nilearn import datasets
from nilearn import decomposition
# Feature Selection
import sklearn_relief as sr

num = 1
adhd_data = datasets.fetch_adhd(n_subjects = num)

print(adhd_data.func)
pca = decomposition.multi_pca.MultiPCA(n_components=20,mask_strategy = 'background')
pca.fit(adhd_data.func)

#Retrieving the components
components = pca.components_

#Using a masker to project into the 3D space
component_img = pca.masker_.inverse_transform(components)
print(component_img.shape)


