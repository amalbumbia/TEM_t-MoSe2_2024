import dm4

dm4data = dm4.DM4File.open("sample.dm4")

tags = dm4data.read_directory()

image_data_tag = tags.named_subdirs['ImageList'].unnamed_subdirs[1].named_subdirs['ImageData']
image_tag = image_data_tag.named_tags['Data']

XDim = dm4data.read_tag_data(image_data_tag.named_subdirs['Dimensions'].unnamed_tags[0])
YDim = dm4data.read_tag_data(image_data_tag.named_subdirs['Dimensions'].unnamed_tags[1])

np_array = np.array(dm4data.read_tag_data(image_tag), dtype=np.uint16)
np_array = np.reshape(np_array, (YDim, XDim))

output_fullpath = "sample.tif"
image = PIL.Image.fromarray(np_array, 'I;16')
image.save(output_fullpath)
