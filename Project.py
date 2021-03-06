{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "import dash\n",
    "import dash_core_components as dcc\n",
    "import dash_html_components as html\n",
    "\n",
    "external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']\n",
    "\n",
    "app = dash.Dash(__name__, external_stylesheets=external_stylesheets)\n",
    "\n",
    "server = app.server\n",
    "\n",
    "app.layout = html.Div([\n",
    "    html.H2('Hello World'),\n",
    "    dcc.Dropdown(\n",
    "        id='dropdown',\n",
    "        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],\n",
    "        value='LA'\n",
    "    ),\n",
    "    html.Div(id='display-value')\n",
    "])\n",
    "\n",
    "@app.callback(dash.dependencies.Output('display-value', 'children'),\n",
    "              [dash.dependencies.Input('dropdown', 'value')])\n",
    "def display_value(value):\n",
    "    return 'You have selected \"{}\"'.format(value)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run_server(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
