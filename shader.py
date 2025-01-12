import bpy

def create_hello_world_shader():
    # Create a new material
    mat = bpy.data.materials.new(name="HelloWorldShader")
    mat.use_nodes = True  # Enable nodes

    # Clear default nodes
    nodes = mat.node_tree.nodes
    for node in nodes:
        nodes.remove(node)

    # Add new nodes
    output_node = nodes.new(type="ShaderNodeOutputMaterial")
    output_node.location = (400, 0)

    emission_node = nodes.new(type="ShaderNodeEmission")
    emission_node.location = (200, 0)

    text_node = nodes.new(type="ShaderNodeTexImage")
    text_node.location = (0, 0)

    # Create a text object texture
    img = bpy.data.images.new("HelloWorldText", width=512, height=512)
    img.generated_type = 'BLANK'

    # Draw "Hello World" on the image
    import bpy_extras
    import bgl
    import gpu
    from gpu_extras.batch import batch_for_shader

    # Set the font size and draw text on the image
    text = "Hello World"
    font_size = 50
    color = (1, 1, 1, 1)  # White

    # Clear the image
    img.pixels = [0] * len(img.pixels)
    
    # Assign image to the text node
    text_node.image = img

    # Link nodes
    links = mat.node_tree.links
    links.new(text_node.outputs['Color'], emission_node.inputs['Color'])
    links.new(emission_node.outputs['Emission'], output_node.inputs['Surface'])

    return mat

# Create the shader and assign it to the active object
if bpy.context.object:
    obj = bpy.context.object
    mat = create_hello_world_shader()
    
    if len(obj.data.materials) == 0:
        obj.data.materials.append(mat)
    else:
        obj.data.materials[0] = mat

print("Hello World Shader created!")
