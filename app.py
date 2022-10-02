from flask import Flask, render_template, request, escape
from sequence_generator import string_to_list, generate_sequences
from itertools import product

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    """
    Display index page at "/"
    """

    return render_template('index.html')

@app.route('/results/', methods=['POST'])
def results():
    """
    Route to send input data.
    """
    fragments_in = request.form["fragments"]
    connections_in = request.form["connections"]

    fragments, invalids = string_to_list(fragments_in)

    if len(invalids) != 0:
        return render_template('index.html',
                                success=False,
                                out_message="Error: Invalid residue(s): '{}'.".format("', '".join(invalids))
                                )

    try:
        connections = int(connections_in)
    except ValueError:
        return render_template('index.html',
                                success=False,
                                out_message='ERROR: Max connections requires a number.'
                                )

    summary, sequences = generate_sequences(fragments, connections)

    return render_template('index.html',
                            success=True,
                            fragments=", ".join(fragments),
                            connections=connections,
                            summary=str(escape(summary)).replace('\n', '<br>'),
                            sequences=str(escape(sequences)).replace('\n', '<br>')
                            )

if __name__ == "__main__":
    app.run(debug=True)