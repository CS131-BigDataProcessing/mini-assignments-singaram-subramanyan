params.str = params.str ?: "Hello World"
params.outputDir = params.outputDir ?: '/results'

workflow {
    Str = Channel.from(params.str)

    Str.view()

    allcaps(Str)
}

process allcaps {
    input:
    val Str

    output:
    path("${params.outputDir}/output.txt")

    script:
    """
    mkdir -p ${params.outputDir}
    python3 -c "print('${Str}'.upper())" > ${params.outputDir}/output.txt
    """
}
