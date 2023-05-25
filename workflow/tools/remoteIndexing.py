from gladier import GladierBaseTool, generate_flow_definition


def launch(**data) -> int:
    import subprocess

    script = '/eagle/projects/APSDataAnalysis/hparraga/laue-indexing/pipeline/pyLaueGo.py'
    mpiCmd = 'mpirun -np 32 python'
    configFile = f"--configFile {data['config_destination_path']}"
    crystalFile = f"--crystFile {data['crystal_destination_path']}"
    geoFile = f"--geoFile {data['geo_destination_path']}"
    inputDir = f"--filefolder {data['input_destination_path']}"
    outputDir = f"--outputFolder {data['output_source_path']}"
    filenamePrefix = f"--filenamePrefix {data['label']}_"
    subprocess.call([mpiCmd, script, configFile, crystalFile, geoFile, inputDir, outputDir, filenamePrefix])


@generate_flow_definition(modifiers={
    launch: {'WaitTime': 1000000,
                      'ExceptionOnActionFailure': True}
})
class RemoteIndexing(GladierBaseTool):

    required_input = [
        'funcx_endpoint_compute',
        'config_destination_path',
        'crystal_destination_path',
        'geo_destination_path',
        'input_destination_path',
        'output_source_path',
        'label'
    ]

    funcx_functions = [
        launch
    ]